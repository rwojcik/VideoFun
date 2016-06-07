/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt.configsPanels;

/**
 *
 * @author Jacek
 */
public class CirclesConfigMemo extends SimpleFilterConfigMemo {
    
    public static final String CONFIG_NAME = "Circles";
    public static final String CONFIG_DESCRIPTION = "Detects circles on image.";

    public CirclesConfigMemo() {
        super(CONFIG_NAME, "FrameEditorCircles");
    }
    
}
