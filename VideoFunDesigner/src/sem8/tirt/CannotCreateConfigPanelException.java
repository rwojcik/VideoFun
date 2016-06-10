/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt;

/**
 * Exception throwing when config panel class is wrong assiociated with viode block.
 * 
 * @author Jacek Skoczylas
 */
public class CannotCreateConfigPanelException extends Exception {

    public CannotCreateConfigPanelException() {
    }

    public CannotCreateConfigPanelException(String message) {
        super(message);
    }

    public CannotCreateConfigPanelException(String message, Throwable cause) {
        super(message, cause);
    }

    public CannotCreateConfigPanelException(Throwable cause) {
        super(cause);
    }
    
    
    
}
