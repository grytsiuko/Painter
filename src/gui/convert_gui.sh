SCRIPT_PATH=$(dirname $0)
pyuic5 $SCRIPT_PATH/gui_root.ui -o $SCRIPT_PATH/gui_root.py
pyuic5 $SCRIPT_PATH/gui_new_file_dialog.ui -o $SCRIPT_PATH/gui_new_file_dialog.py
pyuic5 $SCRIPT_PATH/gui_exit_dialog.ui -o $SCRIPT_PATH/gui_exit_dialog.py