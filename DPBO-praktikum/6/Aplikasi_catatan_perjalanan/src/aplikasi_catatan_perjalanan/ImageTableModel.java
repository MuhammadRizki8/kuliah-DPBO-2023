/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aplikasi_catatan_perjalanan;

/**
 *
 * @author LENOVO
 */
import java.awt.Image;
import java.util.Vector;
import javax.swing.ImageIcon;
import javax.swing.table.DefaultTableModel;

public class ImageTableModel extends DefaultTableModel {

    public ImageTableModel() {
        super();
    }

    public ImageTableModel(Vector data, Vector columnNames) {
        super(data, columnNames);
    }

    @Override
    public Class getColumnClass(int column) {
        if (column == 3) {
            return ImageIcon.class;
        }
        return super.getColumnClass(column);
    }

    @Override
    public boolean isCellEditable(int row, int column) {
        return false;
    }

    public void addRow(Object[] rowData, ImageIcon icon) {
        Object[] newRow = new Object[rowData.length + 1];
        System.arraycopy(rowData, 0, newRow, 0, rowData.length);
        newRow[rowData.length] = icon;
        super.addRow(newRow);
    }

}
