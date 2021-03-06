from PyQt4.Qt import *
import forms.ui_edit_group_name

class EditGroupName(QDialog, forms.ui_edit_group_name.Ui_group_name_dialog):
    
    def __init__(self, cur_group_name, parent=None):
        super(EditGroupName, self).__init__(parent)
        self.setupUi(self)
        self.group_name_le.setText(cur_group_name)
        
    
class EditCovariateName(QDialog, forms.ui_edit_group_name.Ui_group_name_dialog):
    
    def __init__(self, cur_cov_name, parent=None):
        super(EditCovariateName, self).__init__(parent)
        self.setupUi(self)
        self.group_name_le.setText(cur_cov_name)
        self.field_lbl.setText("covariate name:")
        self.setWindowTitle("edit covariate name")