"# TrafficAnalyser"
Le projet est composé d'un seul fichier : cybershark2077.py

Ce fichier est découpé en 2 parties majeures: l'UI et le backend.

Au lancement de l'application, des fichiers JSON sont récupéres. Ces JSON contiennent des informations permettant le decodage des trames.
Elle offre une certaine modularité au logiciel.

Architecture:
├───gui
│   ├───core
│   ├───images
│   │   ├───svg_icons
│   │   └───svg_images
│   ├───themes
│   ├───uis
│   │   ├───columns
│   │   ├───pages
│   │   └───windows
│   │       └───main_window
│   └───widgets
│       ├───py_circular_progress
│       │   └───__pycache__
│       ├───py_credits_bar
│       ├───py_grips
│       ├───py_icon_button
│       ├───py_left_column
│       ├───py_left_menu
│       ├───py_line_edit
│       ├───py_push_button
│       ├───py_table_widget
│       ├───py_title_bar
│       ├───py_toggle
│       ├───py_window
├───models
│   ├───data
├───services
├───trames
├───utils