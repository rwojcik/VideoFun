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
public class CameraSrcConfigMemo extends AbstractVNodeConfigMemo  {
    
    public static final String CONFIG_NAME = "Camera";
    public static final String CONFIG_DESCRIPTION = "Return output from camera.";

    public CameraSrcConfigMemo() {
        super(CameraSrcConfigPanel.class, CONFIG_NAME, 0, 1);
    }
    
}
