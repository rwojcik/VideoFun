# VideoFun

## Short introduction to designer
1. Add video block by buttons on top.
2. You can move and resize viode blocks like windows.
3. To stream output of some block to input other block drag by mouse output first video block and grab it on input secend video block.
4. To merge two video streams into one, put two video streams in some viode block inputs (each viode stream in other input) and click **_M_** button under inputs. It will apear dialog to configure merge type.
5. You can open/save diagrams by options in menu bar. Diagrams are storing in Video Fun Diagram (_*.vfd_ file).

To run created diagram please choose opiton in menu bar:  
`File -> Export to cmd in TCP mode`  
or  
`File -> Export to cmd in UDP mode`  

depending if if you want to use TCP or UDP mode.
After this application will ask you where you want to create *.bat file to run diagram. Please select place inside folder 'VideoFunPy' with files:

+ `block.py`
+ `core.py`
+ `destination.py`
+ `editor.py`
+ `merge.py`
+ `source.py`

It's good to keep folder **_VideoFunPy_** in same location as designer _jar_ file.

You may also export diagram to _XML_ file if you want.

## Documentation
<https://rwojcik.github.io/videoFun/>
