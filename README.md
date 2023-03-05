# This My PC

<div align="center">
        <img src="docs\icon.png" crossorigin >
</div>

<br />

<div align="center">

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)]()
<br />

</div>

> This project is a viewer for network traffic flows, which allows users to analyze frames of a specific protocol. The project supports Layer 2 Ethernet, Layer 3 IPv4, Layer 4 TCP, and Layer 7 HTTP protocols.

> The source code is open so that you can download the source code and set it up with ease if you would like to have your own exclusive environment.

<div align="center">

[![](https://raw.githubusercontent.com/Ammar434/TrafficAnalyser/main/docs/presentation.gif?token=GHSAT0AAAAAAB5XKMND2TJRWFRUIFNXVYMQZAEXWDA)]()
<br />

</div>

## App Screenshots

|                             Trame Visualization                             |                             Left menu                             |                             Information panel                             |                             Export                             |
| :-------------------------------------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------------------------: | :------------------------------------------------------------: |
| <img src="docs\1.png" title="Trame Visualization" width="100%" crossorigin> | <img src="docs\2.png" title="Left menu" width="100%" crossorigin> | <img src="docs\3.png" title="Information panel" width="100%" crossorigin> | <img src="docs\4.png" title="Export" width="100%" crossorigin> |

## Folder Structure

    .
    ├── doc          # All Api doc and gif files
    ├── gui
    ├── models       # Contain JSON model of supported trame type
    ├── services
    ├── trames       # Sample of trame
    ├── utils
    ├── .gitignore
    └── README.md

## Features

- Accepts trace files in text format containing previously - captured bytes over an Ethernet network
- Supports Layer 2 Ethernet, Layer 3 IPv4, Layer 4 TCP, and Layer 7 HTTP protocols
- Offers the option to run in a command window or display in a graphic interface
- Provides an intuitive user experience

## Design and User Experience

This project has been designed with great attention to detail and a focus on providing a great user experience. The interface is easy to use, with clear instructions and intuitive visualizations that make it easy to understand the network traffic flows being analyzed. The user can quickly access the different layers of the protocol stack, and can easily filter and search for specific packets.

<br />

## Built With

- [Python](https://www.python.org/)
- [PyQT5](https://pypi.org/project/PyQt5/)

<br />

## Getting Started

#### Clone Project

```shell
git clone https://github.com/Ammar434/TrafficAnalyser
```

This Command will copy a full project to your local environment

#### Go to the directory

```shell
cd TrafficAnalyser
```

#### Install requirements

```shell
python -r requirements.txt
```

This Command will install the required dependencies.

#### Launch the program

```shell
python main.py
```

## Acknowledgements

I would like to express my sincere gratitude to my university teacher, [Promethee Spathis](https://npa.lip6.fr/~spathis/) for their guidance and support throughout the development of this project.
