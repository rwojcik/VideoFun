/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Point;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.Transferable;
import java.awt.dnd.DnDConstants;
import java.awt.dnd.DropTarget;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ComponentAdapter;
import java.awt.event.ComponentEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.DropMode;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JPanel;
import javax.swing.TransferHandler;
import javax.swing.UIManager;
import javax.swing.event.InternalFrameAdapter;
import javax.swing.event.InternalFrameEvent;

/**
 *
 * @author jskoczyl
 */
public class VNodeFrame extends javax.swing.JInternalFrame implements MouseListener {

    private VideoFunDesigner parent;
    private VNodeMemo memo;
    private JButton[] inputsButtons;
    private JButton[] outputsButtons;

    /**
     * Creates new form AbstractVNodeFrame
     */
    public VNodeFrame(VNodeMemo memo) {
        super(memo.getConfigMemo().getConfigName(),
                true, //resizable
                true, //closable
                true, //maximizable
                true);//iconifiable
        this.memo = memo;
        changeSizeAndDimensionsToMemo();

        initComponents();
        //jPanel2.add(createConfigPanel(), BorderLayout.CENTER);
        addInOutsButtons(memo);
        addInternalFrameListener(new InternalFrameAdapter() {
            @Override
            public void internalFrameClosing(InternalFrameEvent e) {
                if (parent == null) {
                    return;
                }
                for (JButton b : inputsButtons) {
                    parent.deleteAllLinksWithInLink(b.getName());
                }
                for (JButton b : outputsButtons) {
                    parent.deleteAllLinksWithInLink(b.getName());
                }
            }
        });
    }

    public VNodeMemo getMemo() {
        memo.setLocation(getLocation());
        memo.setSize(getSize());
        return memo;
    }

    public Point getInputLocationOnScreen_orNull(int n) {
        return getLocationOnScreenOfMiddleOfButton_orNull(inputsButtons[n]);
    }

    public Point getOutputLocationOnScreen_orNull(int n) {
        return getLocationOnScreenOfMiddleOfButton_orNull(outputsButtons[n]);
    }

    protected Point getLocationOnScreenOfMiddleOfButton_orNull(JButton b) {
        try {
            Point p = b.getLocationOnScreen();
            p.x += b.getWidth() / 2;
            p.y += b.getHeight() / 2;
            return p;
        } catch (java.awt.IllegalComponentStateException e) {
            return null;
        }
    }

    public void setParent(VideoFunDesigner parent) {
        this.parent = parent;
        addComponentListener(new ComponentAdapter() {
            @Override
            public void componentMoved(ComponentEvent e) {
                parent.repaint();
            }
        });
    }

    private void addInOutsButtons(VNodeMemo memo1) {
        inputsButtons = new JButton[memo1.getInputsNum()];
        for (int i = 0; i < memo1.getInputsNum(); i++) {
            jPanelInputs.add(inputsButtons[i] = createInButton(i));
            inputsButtons[i].addMouseListener(this);
        }
        outputsButtons = new JButton[memo1.getOutputsNum()];
        for (int i = 0; i < memo1.getOutputsNum(); i++) {
            jPanelOutputs.add(outputsButtons[i] = createOutButton(i));
            outputsButtons[i].addMouseListener(this);
        }
    }

    private JButton createOutButton(final int i) {
        final JButton button = new JButton("Out " + i);
        final String outLink = VideoLink.toOutputLink(memo.getVnodeNumber(), i);
        button.setName(outLink);
        button.setTransferHandler(new TransferHandler() {
            @Override
            public int getSourceActions(JComponent c) {
                return DnDConstants.ACTION_COPY_OR_MOVE;
            }

            @Override
            protected Transferable createTransferable(JComponent c) {
                Transferable t = new StringSelection(outLink);
                return t;
            }

            @Override
            protected void exportDone(JComponent source, Transferable data, int action) {
                super.exportDone(source, data, action);
                // Decide what to do after the drop has been accepted
            }
        });
        button.addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                JButton button = (JButton) e.getSource();
                TransferHandler handle = button.getTransferHandler();
                handle.exportAsDrag(button, e, TransferHandler.COPY);
            }
        });
        return button;
    }

    private JButton createInButton(final int i) {
        final JButton button = new JButton("In " + i);
        final String inLink = VideoLink.toInputLink(memo.getVnodeNumber(), i);
        button.setName(inLink);
        button.setTransferHandler(new TransferHandler() {
            @Override
            public boolean canImport(TransferHandler.TransferSupport info) {
                // we only import Strings
                if (!info.isDataFlavorSupported(DataFlavor.stringFlavor)) {
                    return false;
                }
                String data = getText_orNull(info);
                return VideoLink.matchPattern(data);
            }

            private String getText_orNull(TransferHandler.TransferSupport info) {
                String data;
                try {
                    data = (String) info.getTransferable().getTransferData(DataFlavor.stringFlavor);
                } catch (Exception e) {
                    data = null;
                }
                return data;
            }

            @Override
            public boolean importData(TransferHandler.TransferSupport support) {
                String outLink = getText_orNull(support);
                makeLink(inLink, outLink);
                return true;
            }

        });
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                parent.deleteAllLinksWithInLink(inLink);
            }
        });
        return button;
    }

    private void makeLink(String inLink, String outLink) {
        try {
            VideoLink link = new VideoLink(inLink, outLink);
            parent.deleteAllLinksWithInLink(inLink.startsWith("in") ? inLink : outLink);
            parent.addVideoLink(link);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    protected JPanel createConfigPanel() {
        try {
            return memo.getConfigMemo().createJPanel();
        } catch (CannotCreateConfigPanelException ex) {
            ex.printStackTrace();
            final JPanel jPanel = new JPanel();
            jPanel.setBackground(Color.RED);
            return jPanel;
        }
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

        jPanelInputs = new javax.swing.JPanel();
        jPanel2 = new javax.swing.JPanel();
        jPanelOutputs = new javax.swing.JPanel();

        getContentPane().setLayout(new java.awt.GridBagLayout());

        jPanelInputs.setLayout(new javax.swing.BoxLayout(jPanelInputs, javax.swing.BoxLayout.Y_AXIS));
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.fill = java.awt.GridBagConstraints.BOTH;
        gridBagConstraints.weighty = 1.0;
        getContentPane().add(jPanelInputs, gridBagConstraints);

        jPanel2.setLayout(new java.awt.BorderLayout());
        jPanel2.add(createConfigPanel(), BorderLayout.CENTER);
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.fill = java.awt.GridBagConstraints.BOTH;
        gridBagConstraints.weightx = 1.0;
        gridBagConstraints.weighty = 1.0;
        getContentPane().add(jPanel2, gridBagConstraints);

        jPanelOutputs.setLayout(new javax.swing.BoxLayout(jPanelOutputs, javax.swing.BoxLayout.Y_AXIS));
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.fill = java.awt.GridBagConstraints.BOTH;
        gridBagConstraints.weighty = 1.0;
        getContentPane().add(jPanelOutputs, gridBagConstraints);

        pack();
    }// </editor-fold>//GEN-END:initComponents


    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanelInputs;
    private javax.swing.JPanel jPanelOutputs;
    // End of variables declaration//GEN-END:variables

    private void changeSizeAndDimensionsToMemo() {
        if(memo.getLocation_orNull() != null) {
            setLocation(memo.getLocation_orNull());
        }
        if(memo.getSize_orNull() != null) {
            setSize(memo.getSize_orNull());
        } else {
            setSize(200, 150);
        }
    }

    @Override
    public void mouseClicked(MouseEvent e) {
    }

    @Override
    public void mousePressed(MouseEvent e) {
    }

    @Override
    public void mouseReleased(MouseEvent e) {
    }

    @Override
    public void mouseEntered(MouseEvent e) {
        parent.repaint();
    }

    @Override
    public void mouseExited(MouseEvent e) {
        parent.repaint();
    }
}
