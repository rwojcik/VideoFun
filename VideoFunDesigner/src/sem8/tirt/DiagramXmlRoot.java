/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt;

import java.util.ArrayList;
import javax.xml.bind.annotation.XmlRootElement;

/**
 *
 * @author jskoczyl
 */
@XmlRootElement
    class DiagramXmlRoot {

        private ArrayList<VNodeMemo> vNodeFrames;
        private ArrayList<VideoLink> videoLinks;

    public DiagramXmlRoot() {
        vNodeFrames = new ArrayList<VNodeMemo>();
        videoLinks = new  ArrayList<VideoLink>();
    }

        public DiagramXmlRoot(ArrayList<VNodeMemo> vNodeFrames, ArrayList<VideoLink> videoLinks) {
            this.vNodeFrames = vNodeFrames;
            this.videoLinks = videoLinks;
        }

    public ArrayList<VNodeMemo> getvNodeFrames() {
        return vNodeFrames;
    }

    public void setvNodeFrames(ArrayList<VNodeMemo> vNodeFrames) {
        this.vNodeFrames = vNodeFrames;
    }

    public ArrayList<VideoLink> getVideoLinks() {
        return videoLinks;
    }

    public void setVideoLinks(ArrayList<VideoLink> videoLinks) {
        this.videoLinks = videoLinks;
    }
        
        

    }