/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt.configsPanels;

import sem8.tirt.AbstractVNodeConfigMemo;

/**
 *
 * @author jskoczyl
 */
public class GreyConfigMemo extends SimpleFilterConfigMemo {
    
    public static final String CONFIG_NAME = "Grey Colors";
    public static final String CONFIG_DESCRIPTION = "Changes colors of image to gray scale.";

    public GreyConfigMemo() {
        super(CONFIG_NAME, "FrameEditorGreyscale");
    }
    
}
