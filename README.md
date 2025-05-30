# Spotify Keychains

This project generates custom 3D keychain models with Spotify codes, ready for 3D printing.

## How does it work?

1. The user enters a Spotify link (song, album, artist, or playlist).
2. The user selects a keychain model from several available options.
3. The script downloads the corresponding Spotify code and converts it into 3D bars on the base model.
4. The final model is exported as an STL file, ready for printing.

## Requirements

- Python 3.8+
- [CadQuery](https://cadquery.readthedocs.io/en/latest/)
- [Pillow](https://pypi.org/project/Pillow/)
- [requests](https://pypi.org/project/requests/)

Install dependencies with:

```bash
pip install cadquery Pillow requests
```

## Important files

- `Main.py`: Main script to generate the models.
- `Spotify_circle_Model.step` and other `.step` models: Base models for the keychains.
- `finished_models/` folder: Generated STL files are saved here.

## Usage

Run the main script:

```bash
python Main.py
```

Follow the on-screen instructions to enter the Spotify link, model name, and select the keychain type.

The generated STL file will be in the `finished_models/` folder.

## Credits

Developed by CodeCrellan.
Based in code of sDesigns from MakerWorld