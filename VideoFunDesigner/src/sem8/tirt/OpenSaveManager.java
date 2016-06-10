/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt;

import java.awt.Component;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.net.DatagramSocket;
import java.net.ServerSocket;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.Marshaller;
import javax.xml.bind.annotation.XmlRootElement;

/**
 * Class implementing open/save with gui dialogs about it.
 * 
 * @author jskoczyl
 */
public class OpenSaveManager {

    private Component parentComponent;
    private JFileChooser chooser;
    private File lastSave_orNull;
    private FileNameExtensionFilter batFileFilter;
    private FileNameExtensionFilter diagramFileFilter;
    private FileNameExtensionFilter xmlFileFilter;

    public OpenSaveManager(Component parentComponent, JFileChooser chooser) {
        this.parentComponent = parentComponent;
        this.chooser = chooser;
        lastSave_orNull = null;
        createAndAddFileFilters(chooser);
    }

    private void createAndAddFileFilters(JFileChooser chooser1) {
        batFileFilter = new FileNameExtensionFilter("Bat files", "bat");
        diagramFileFilter = new FileNameExtensionFilter("Video Fun Diagrams", "vfd");
        xmlFileFilter = new FileNameExtensionFilter("Xml files", "xml");
        chooser1.addChoosableFileFilter(batFileFilter);
        chooser1.addChoosableFileFilter(diagramFileFilter);
        chooser1.addChoosableFileFilter(xmlFileFilter);
    }

    public void save(File file, ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks) throws IOException {
        ArrayList<VNodeMemo> memos = toMemos(vNodeFrames);
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file))) {
            out.writeObject(memos);
            out.writeObject(videoLinks);
        }
    }

    private ArrayList<VNodeMemo> toMemos(ArrayList<VNodeFrame> vNodeFrames) {
        ArrayList<VNodeMemo> memos = new ArrayList<VNodeMemo>();
        for (VNodeFrame n : vNodeFrames) {
            memos.add(n.getMemo());
        }
        return memos;
    }

    public ArrayList<VNodeMemo> readInto(File file, ArrayList<VideoLink> videoLinks) throws IOException, ClassNotFoundException {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(file))) {
            ArrayList<VNodeMemo> memos = (ArrayList<VNodeMemo>) in.readObject();
            ArrayList<VideoLink> readed_VideoLinks = (ArrayList<VideoLink>) in.readObject();
            videoLinks.clear();
            for (VideoLink l : readed_VideoLinks) {
                videoLinks.add(l);
            }
            return memos;
        }
    }

    public void gui_save(boolean saveAs, ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks) {
        File file = null;
        if (!saveAs) {
            setDefaultFileFilterToDiagram();
            file = lastSave_orNull != null ? lastSave_orNull : askFile("Save diagram");
            file = ensureFileExtension(file, ".vfd");
        } else {
            file = askFile("Save diagram");
        }
        if (file == null) {
            return;
        }
        lastSave_orNull = file;
        try {
            save(file, vNodeFrames, videoLinks);
        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(parentComponent, "Exception messege: " + e.getMessage(), "Not able to save", JOptionPane.ERROR_MESSAGE);
        }
    }

    public ArrayList<VNodeMemo> gui_openInto_orNull(ArrayList<VideoLink> videoLinks) {
        setDefaultFileFilterToDiagram();
        File file = askFile("Open diagram");
        if (file == null) {
            return null;
        }
        lastSave_orNull = file;
        try {
            return readInto(file, videoLinks);
        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(parentComponent, "Exception messege: " + e.getMessage(), "Not able to open", JOptionPane.ERROR_MESSAGE);
            return null;
        }
    }
    
    private void setDefaultFileFilterToBat() {
        chooser.setFileFilter(batFileFilter);
    }
    
    private void setDefaultFileFilterToDiagram() {
        chooser.setFileFilter(diagramFileFilter);
    }
    
    private void setDefaultFileFilterToXml() {
        chooser.setFileFilter(xmlFileFilter);
    }

    private File askFile(String aproveButtonText) {
        return askFile(aproveButtonText, null);
    }

    private File askFile(String aproveButtonText, File dir_orNull) {
        if (dir_orNull != null) {
            chooser.setCurrentDirectory(dir_orNull);
        }
        int answer = chooser.showDialog(parentComponent, aproveButtonText);
        if (answer == JFileChooser.APPROVE_OPTION) {
            return chooser.getSelectedFile();
        }
        return null;
    }

    void exportXml(ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks) {
        setDefaultFileFilterToXml();
        File file = askFile("Export xml");
        file = ensureFileExtension(file, ".xml");
        if (file == null) {
            return;
        }
        try {
            JAXBContext context = JAXBContext.newInstance(DiagramXmlRoot.class);

            Marshaller m = context.createMarshaller();
            m.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            ArrayList<VNodeMemo> memos = toMemos(vNodeFrames);
            DiagramXmlRoot root = new DiagramXmlRoot(memos, videoLinks);

            m.marshal(root, new FileOutputStream(file));
        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(parentComponent, "Exception messege: " + e.getMessage(), "Not able to export xml", JOptionPane.ERROR_MESSAGE);
        }
    }

    File exportCmd(ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks, boolean asTcp) {
        File cmdFile = newCmdFile(asTcp);
        if (cmdFile == null) {
            return null;
        }
        findFreeTcpsPorts(videoLinks);
        try (PrintWriter out = new PrintWriter(cmdFile)) {
            for (VNodeFrame vnode : vNodeFrames) {
                VNodeMemo memo = vnode.getMemo();
                int[] ins = createIns(memo, videoLinks);
                int[] outs = createOuts(memo, videoLinks);
                String cmd = memo.getConfigMemo().getRunCmd(ins, outs, asTcp);
                out.println(cmd);
                System.out.println(cmd);
            }
        } catch (IOException ex) {
            ex.printStackTrace();
            return null;
        }
        return cmdFile;
    }

    private File newCmdFile(boolean asTcp) {
        File[] toTestFiles = new File[]{
            new File("VideoFunPy"),
            new File("../VideoFunPy")
        };
        File dir = null;
        for (File f : toTestFiles) {
            if (f.exists()) {
                dir = f;
                break;
            }
        }
        String text = asTcp ? "Gen TCP cmd" : "Gen UDP cmd";
        setDefaultFileFilterToBat();
        File file = askFile(text, dir);
        file = ensureFileExtension(file, ".bat");
        return file;
    }

    private void findFreeTcpsPorts(ArrayList<VideoLink> videoLinks) {
        int port = 5005;
        for (VideoLink link : videoLinks) {
            while (!available(port)) {
                port++;
            }
            link.setTmpTcp(port);
            System.out.println("got tcp: " + port);
            port++;
        }
    }

    public static boolean available(int port) {
        ServerSocket ss = null;
        DatagramSocket ds = null;
        try {
            ss = new ServerSocket(port);
            ss.setReuseAddress(true);
            ds = new DatagramSocket(port);
            ds.setReuseAddress(true);
            return true;
        } catch (IOException e) {
        } finally {
            if (ds != null) {
                ds.close();
            }

            if (ss != null) {
                try {
                    ss.close();
                } catch (IOException e) {
                    /* should not be thrown */
                }
            }
        }

        return false;
    }

    private int[] createIns(VNodeMemo memo, ArrayList<VideoLink> videoLinks) {
        int[] result = new int[memo.getInputsNum()];
        for (int i = 0; i < result.length; i++) {
            result[i] = -1;
        }
        int index = 0;
        for (VideoLink link : videoLinks) {
            if (link.getDstVNode() == memo.getVnodeNumber()) {
                result[index++] = link.getTmpTcp();
            }
        }
        return result;
    }

    private int[] createOuts(VNodeMemo memo, ArrayList<VideoLink> videoLinks) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int index = 0;
        for (VideoLink link : videoLinks) {
            if (link.getSrcVNode() == memo.getVnodeNumber()) {
                result.add(link.getTmpTcp());
            }
        }
        int[] r = new int[result.size()];
        int i = 0;
        for (Integer v : result) {
            r[i++] = v;
        }
        return r;
    }

    void exportCmdAndRun(ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks, boolean asTcp) {
        File file = exportCmd(vNodeFrames, videoLinks, asTcp);
        if (file != null) {
            try {
                Process exec = Runtime.getRuntime().exec("cmd");
                PrintStream out = new PrintStream(exec.getOutputStream());
                out.println("start \"\" \"" + file.getAbsolutePath() + "\"");
                System.out.println("start \"\" \"" + file.getAbsolutePath() + "\"");
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }

    private File ensureFileExtension(File file, String extWithDot) {
        if(file == null) {
            return null;
        }
        if(!file.getName().endsWith(extWithDot)) {
            return new File(file.getParent(), file.getName() + extWithDot);
        }
        return file;
    }
}
