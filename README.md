# KnapSack Visualizer

KnapSack Visualizer lets you visualize & trace solutions to the knapsack problem with a GUI.

## Usage
- You must have PyQt5 installed. [Link](https://doc.bccnsoft.com/docs/PyQt5/installation.html)
```bash
pip3 install PyQt5
git clone https://github.com/madelesi/knapsack-visualizer.git
cd knapsack-visualizer/knapsack_visualizer
python3 gui.py
 ```

## Dev Quick-start
- Beyond PyQt5 you will want to install pyuic5 and probably qtdesigner for development.
- The general structure:
```bash
.
├── knapsack.py # put your algorithms here. (You have to create a class with get_cell_value() and get_cell_parents(), and 
                # gui_horizontal_headers/gui_vert_headers)
├── alg_input_windows
│   ├── knapsack_input_window # make a similiar file that is a window, take in the main window(so you can change its .alg) as input and 
│   └──                       # set its main_window.alg attribute to your own algorithm class (which you give arguments from your input # window)
│   └── knapsack_input.ui     
│   └── knapsack_input_GEN.py # the optional .ui file is created from the qtdesigner GUI., and the *_GEN.py is generated from that.
├── gui.py # Add your window to ALG_TO_WINDOW and take a look at on_alg_btn()

``` 
- [Quick Guide on PyQt5 Layout](http://zetcode.com/gui/pyqt5/layout/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
