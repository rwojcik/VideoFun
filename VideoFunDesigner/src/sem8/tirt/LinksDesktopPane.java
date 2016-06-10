/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Point;
import java.awt.RenderingHints;
import javax.swing.JDesktopPane;

/**
 * This class paints links between blocks on screen.
 * 
 * @author Jacek Skoczylas
 */
public class LinksDesktopPane extends JDesktopPane {
    
    private VideoFunDesigner parent;

    public void setParent(VideoFunDesigner parent) {
        this.parent = parent;
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g); //To change body of generated methods, choose Tools | Templates.
        if(parent == null) {
            return;
        }
        prepareLinesPaint(g);
        for(VideoLink link : parent.getVideoLinks()) {
            VNodeFrame srcNode = parent.getVNodeFrame(link.getSrcVNode());
            VNodeFrame dstNode = parent.getVNodeFrame(link.getDstVNode());
            paintLink(g, srcNode, dstNode, link.getSrcOutput(), link.getDstInput());
        }
    }

    private void prepareLinesPaint(Graphics g) {
        g.setColor(Color.RED);
        if(g instanceof Graphics2D) {
            Graphics2D g2 = (Graphics2D) g;
            g2.setStroke(new BasicStroke(3.5f));
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        }
    }

    /**
     * Paints a single video link betwwen two given blocks: <code>src</code> and <code>dst</code>
     * 
     * @param g graphics contex to paint on
     * @param src source video block
     * @param dst destination video block
     * @param srcNum number of source output
     * @param dstNum number od destination input
     */
    private void paintLink(Graphics g, VNodeFrame src, VNodeFrame dst, int srcNum, int dstNum) {
        Point p1 = src.getOutputLocationOnScreen_orNull(srcNum);
        Point p2 = dst.getInputLocationOnScreen_orNull(dstNum);
        if(p1 == null || p2 == null) {
            return;
        }
        p1.x -= getLocationOnScreen().x;
        p1.y -= getLocationOnScreen().y;
        p2.x -= getLocationOnScreen().x;
        p2.y -= getLocationOnScreen().y;
        g.drawLine(p1.x, p1.y, p2.x, p2.y);
    }
    
}
