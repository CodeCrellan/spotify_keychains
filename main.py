import cadquery as cq
import requests
import io
from PIL import Image
import tools


models_available = ["Spotify_Basic_Model", "Spotify_Half_Heart_Left_Model", "Spotify_Half_Heart_Right_Model", "Spotify_Heart_Model", "Spotify_Model_test"]

if __name__ == '__main__':

    share_link = input("Enter link of song, album, artist or playlist: ")
    model_name = input("Enter name of model: ")
    
    
    print("Available Models:")
    print("0. Spotify Symbol")
    print("1. Half Heart (Left)")
    print("2. Half Heart (Right)")
    print("3. Heart Symbol")
    print("4. Shape Test Model")
    model_selection_index = input("Select one of the models above by typing its Index: ").strip().lower()

    link_data = tools.get_link_data(share_link)

    if len(link_data) != 2:
        print("Something went wrong while parsing the URL.")
        exit(-1)

    code_url = "https://www.spotifycodes.com/downloadCode.php?uri=jpeg%2F000000%2Fwhite%2F640%2Fspotify%3A" + link_data[0] + "%3A" + link_data[1]

    response = requests.get(code_url)

    if not response.ok or not response.content:
        print("Something went wrong while fetching the Spotify code.")
        exit(-1)

    img = Image.open(io.BytesIO(response.content)).crop((160, 0, 640-31, 160))
    width, height = img.size

    pix = img.load()

    bar_heights = []
    max_height_of_single_bar = 0

    for x in range(width):

        at_bar = False
        curr_height = 0

        for y in range(height):
            if pix[x,y][0] > 20 or pix[x,y][1] > 20 or pix[x,y][2] > 20:
                at_bar = True
                curr_height += 1

        if at_bar and curr_height > max_height_of_single_bar:
            max_height_of_single_bar = curr_height/20
        elif not at_bar and max_height_of_single_bar > 0:
            bar_heights.append(max_height_of_single_bar)
            max_height_of_single_bar = 0

    print(f"There are {len(bar_heights)} bars of heights {bar_heights}")

    if model_selection_index.isdigit() and int(model_selection_index) < len(models_available):
        base_model = models_available[int(model_selection_index)]
    else:
        print("Invalid model selection, using default Spotify Symbol model.")
        base_model = "Spotify_Basic_Model"
        
    base_model = cq.importers.importStep(f'{base_model}.step')

    current_bar = 0

    for bar in bar_heights:
        base_model = (
            base_model.pushPoints([(15.5 + current_bar * 1.88, 7.5)])
            .sketch()
            .slot(9 / 5 * bar, 1, 90)
            .finalize()
            .extrude(4)
        )
        current_bar += 1

    if model_name:
        cq.exporters.export(base_model, f'finished_models/{model_name}.stl')
    else:   
        cq.exporters.export(base_model, 'finished_models/model_name.stl')
