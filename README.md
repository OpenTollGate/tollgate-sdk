# Composite action for building SDK

This repository contains a composite action (`action.yml`), which uses the OpenWRT SDK to package the individual TollGate modules in their respective actions. This composite action uploads the package (`.ipk`) to blossom and creates a nostr event announcing the blossom server and file hash for later download. You can later use the imagebuilder to download these packages and install them in an OpenWRT image for a release.

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
