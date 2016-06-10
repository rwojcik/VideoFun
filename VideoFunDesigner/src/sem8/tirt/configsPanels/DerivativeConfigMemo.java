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
public class DerivativeConfigMemo extends SimpleFilterConfigMemo {
    
    public static final String CONFIG_NAME = "Derivative";
    public static final String CONFIG_DESCRIPTION = "Make Derivative on image.";

    public DerivativeConfigMemo() {
        super(CONFIG_NAME, "FrameEditorDerivative");
    }
    
}
