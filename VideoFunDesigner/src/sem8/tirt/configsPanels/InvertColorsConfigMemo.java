/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt.configsPanels;

import sem8.tirt.AbstractVNodeConfigMemo;

/**
 *
 * @author Jacek Skoczylas
 */
public class InvertColorsConfigMemo extends SimpleFilterConfigMemo {
    
    public static final String CONFIG_NAME = "Invert Colors";
    public static final String CONFIG_DESCRIPTION = "Iverts colors of image.";
    private static final long serialVersionUID = 3807724787881483143L;

    public InvertColorsConfigMemo() {
        super(CONFIG_NAME, "FrameEditorColorInversion");
    }
    
}
