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
public class RevertColorsConfigMemo extends AbstractVNodeConfigMemo {
    
    public static final String CONFIG_NAME = "Color Revert";
    public static final String CONFIG_DESCRIPTION = "Reverts the colors on video in RGB space.";

    public RevertColorsConfigMemo() {
        super(RevertColorsConfigPanel.class, CONFIG_NAME);
    }
    
}
