/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt.configsPanels;

import sem8.tirt.AbstractVNodeConfigMemo;

/**
 * Base class for video blocks with no parameters.
 * 
 * @author Jacek Skoczylas
 */
public abstract class SimpleFilterConfigMemo extends AbstractVNodeConfigMemo {
    
    private String guiName;
    private String editorName;

    public SimpleFilterConfigMemo(String guiName, String editorName) {
        super(SimpleFilterConfigPanel.class, guiName);
        this.guiName = guiName;
        this.editorName = editorName;
    }

    @Override
    protected String getRunCmdWithParams(StringBuilder builder) {
        builder.append("  -editor ");
        builder.append(editorName);
        return builder.toString();
    }

    public String getGuiName() {
        return guiName;
    }
    
}