/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt.configsPanels;

/**
 *
 * @author Jacek Skoczylas
 */
public class BlurConfigPanel extends javax.swing.JPanel {

    BlurConfigMemo memo;
    
    /**
     * Creates new form BlurConfigPanel
     */
    public BlurConfigPanel(BlurConfigMemo m) {
        this.memo = m;
        initComponents();
        
        jSpinner1.setValue(memo.getBlurSizeX());
        jSpinner2.setValue(memo.getBlurSizeY());
        jComboBox1.setSelectedIndex(memo.getBlurType());
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {
        java.awt.GridBagConstraints gridBagConstraints;

        jLabel1 = new javax.swing.JLabel();
        jComboBox1 = new javax.swing.JComboBox<String>();
        jLabel2 = new javax.swing.JLabel();
        jSpinner1 = new javax.swing.JSpinner();
        jSpinner2 = new javax.swing.JSpinner();

        setLayout(new java.awt.GridBagLayout());

        jLabel1.setText("Blur type: ");
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        gridBagConstraints.weightx = 0.5;
        gridBagConstraints.weighty = 0.5;
        add(jLabel1, gridBagConstraints);

        jComboBox1.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "Gaussian", "Usuwanie szumu" }));
        jComboBox1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jComboBox1ActionPerformed(evt);
            }
        });
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridwidth = 2;
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        gridBagConstraints.weightx = 0.5;
        gridBagConstraints.weighty = 0.5;
        add(jComboBox1, gridBagConstraints);

        jLabel2.setText("Blur size: ");
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridx = 0;
        gridBagConstraints.gridy = 1;
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        gridBagConstraints.weightx = 0.5;
        gridBagConstraints.weighty = 0.5;
        add(jLabel2, gridBagConstraints);

        jSpinner1.setModel(new javax.swing.SpinnerNumberModel(11, 1, 10000, 2));
        jSpinner1.addChangeListener(new javax.swing.event.ChangeListener() {
            public void stateChanged(javax.swing.event.ChangeEvent evt) {
                jSpinner1StateChanged(evt);
            }
        });
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridx = 1;
        gridBagConstraints.gridy = 1;
        gridBagConstraints.anchor = java.awt.GridBagConstraints.LINE_START;
        gridBagConstraints.weightx = 0.5;
        gridBagConstraints.weighty = 0.5;
        add(jSpinner1, gridBagConstraints);

        jSpinner2.setModel(new javax.swing.SpinnerNumberModel(11, 1, 10000, 2));
        jSpinner2.addChangeListener(new javax.swing.event.ChangeListener() {
            public void stateChanged(javax.swing.event.ChangeEvent evt) {
                jSpinner2StateChanged(evt);
            }
        });
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridx = 2;
        gridBagConstraints.gridy = 1;
        gridBagConstraints.weightx = 0.5;
        add(jSpinner2, gridBagConstraints);
    }// </editor-fold>//GEN-END:initComponents

    private void jComboBox1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jComboBox1ActionPerformed
        memo.setBlurType(jComboBox1.getSelectedIndex());
    }//GEN-LAST:event_jComboBox1ActionPerformed

    private void jSpinner1StateChanged(javax.swing.event.ChangeEvent evt) {//GEN-FIRST:event_jSpinner1StateChanged
        memo.setBlurSizeX((Integer)jSpinner1.getValue());
    }//GEN-LAST:event_jSpinner1StateChanged

    private void jSpinner2StateChanged(javax.swing.event.ChangeEvent evt) {//GEN-FIRST:event_jSpinner2StateChanged
        memo.setBlurSizeY((Integer)jSpinner2.getValue());
    }//GEN-LAST:event_jSpinner2StateChanged


    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JComboBox<String> jComboBox1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JSpinner jSpinner1;
    private javax.swing.JSpinner jSpinner2;
    // End of variables declaration//GEN-END:variables

    /*private void updateBlurSize() {
        memo.setBlurSizeX((Integer)jSpinner1.getValue());
        memo.setBlurSizeY((Integer)jSpinner2.getValue());
    }*/
}
