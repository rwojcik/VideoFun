/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt;

import java.io.Serializable;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author Jacek Skoczylas
 */
public class VideoLink implements Serializable {
    
    public static final Pattern VIDEO_LINK_PATTERN = Pattern.compile("[in|out]:\\/\\/([\\d]+):([\\d]+)");
    
    public static String toInputLink(int dstVNode, int dstInput) {
        return String.format("in://%d:%d", dstVNode, dstInput);
    }
    
    public static String toOutputLink(int srcVNode, int srcOutput) {
        return String.format("out://%d:%d", srcVNode, srcOutput);
    }

    static boolean matchPattern(String data) {
        return VIDEO_LINK_PATTERN.matcher(data).find();
    }
    
    private int srcVNode;
    private int srcOutput;
    private int dstVNode;
    private int dstInput;
    private int tmpTcp;

    public VideoLink(int srcVNode, int srcOutput, int dstVNode, int dstInput) {
        this.srcVNode = srcVNode;
        this.srcOutput = srcOutput;
        this.dstVNode = dstVNode;
        this.dstInput = dstInput;
    }

    public VideoLink(String dstUrl, String srcUrl) {
       if(dstUrl.startsWith("out") && srcUrl.startsWith("in")) {
           String tmp = dstUrl;
           dstUrl = srcUrl;
           srcUrl = tmp;
       }
        Matcher srcMatcher = VIDEO_LINK_PATTERN.matcher(srcUrl);
        Matcher dstMatcher = VIDEO_LINK_PATTERN.matcher(dstUrl);
        if(!srcMatcher.find() || !dstMatcher.find()) {
            throw new IllegalArgumentException("given links not mathcing to pattern");
        }
        srcVNode = Integer.parseInt(srcMatcher.group(1));
        srcOutput = Integer.parseInt(srcMatcher.group(2));
        dstVNode = Integer.parseInt(dstMatcher.group(1));
        dstInput = Integer.parseInt(dstMatcher.group(2));
    }

    public int getSrcVNode() {
        return srcVNode;
    }

    public void setSrcVNode(int srcVNode) {
        this.srcVNode = srcVNode;
    }

    public int getSrcOutput() {
        return srcOutput;
    }

    public void setSrcOutput(int srcOutput) {
        this.srcOutput = srcOutput;
    }

    public int getDstVNode() {
        return dstVNode;
    }

    public void setDstVNode(int dstVNode) {
        this.dstVNode = dstVNode;
    }

    public int getDstInput() {
        return dstInput;
    }

    public void setDstInput(int dstInput) {
        this.dstInput = dstInput;
    }

    boolean cotainsUrl(String inLink) {
        Matcher m = VIDEO_LINK_PATTERN.matcher(inLink);
        if(!m.find()) {
            return false;
        }
        int vnode = Integer.parseInt(m.group(1));
        int put = Integer.parseInt(m.group(2));
        if(inLink.startsWith("in")) {
            return dstVNode == vnode && dstInput == put;
        } else {
            return srcVNode == vnode && srcOutput == put;
        }
    }

    public int getTmpTcp() {
        return tmpTcp;
    }

    public void setTmpTcp(int tmpTcp) {
        this.tmpTcp = tmpTcp;
    }
    
}
