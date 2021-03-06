#Author-Catherine Jones
#Description-Creates Finger joint boxes suitable for lazer cutting

import adsk.core, adsk.fusion, adsk.cam, traceback,os, sys
sys.path.append(os.path.dirname(__file__))

# global set of event handlers to keep them referenced for the duration of the command
handlers = []
app = adsk.core.Application.get()
if app:
    ui = app.userInterface
DEFAULT_WIDTH = '100 mm'
DEFAULT_HEIGHT = '100 mm'
DEFAULT_DEPTH =  '100 mm'
DEFAULT_THICKNESS = '6 mm'
DEFAULT_NOTCH_WIDTH = '10 mm'
DEFAULT_COMPONENT = app.activeProduct.rootComponent

OFFSET = 1 #The gap between the faces

    

def drawAll(x, y, width, height, depth, thickness,notch_width,  lines):
    print("draw all")
    print("thickness = ", thickness)
    x = 0
    y = 0
    
    
    # The minimum notch width cannot be less than the material thickness
    if (notch_width < thickness):
        notch_width = thickness
        
    # The maximum notch width cannot be larger than 20% of the size of the smallest dimension
    smallest_side = min(width,height,depth)

    if (notch_width > (smallest_side * 0.2)):
        notch_width = smallest_side * 0.2
        
    
    drawFront(x, y, width, height, thickness, notch_width,  lines)
    drawLeft(x, y, width, height, depth, thickness, notch_width, lines)
    drawTop(x, y, width, depth, thickness, notch_width, lines)
    drawBack(x, y, width,  height, thickness, notch_width, lines )
    drawRight(x, y, width, height, depth, thickness, notch_width, lines)
    drawBottom(x, y, width, depth, thickness, notch_width, lines )
    
 


  #  genHorizontalLinePoints(x_origin, y_origin, length, notch_width, thickness):   
# Front 
def drawFront(x, y, width, height, thickness, notch_width, lines):
     #Base Horizontal
     drawNotchedLine(genHorizontalLinePoints(x,
                                             y,
                                             width,
                                             notch_width,
                                             thickness,
                                             True ),
                                             lines)
                                             
     drawNotchedLine(genVerticalLinePoints(width,
                                           height,
                                           -height,
                                           notch_width,
                                           thickness,
                                           True ),
                                           lines)
                                           
     drawNotchedLine(genHorizontalLinePoints(width,
                                             height,
                                             -width,
                                             notch_width,
                                             thickness, 
                                             True),
                                             lines)
     drawNotchedLine(genVerticalLinePoints(x,
                                           y,
                                           height,
                                           notch_width,
                                           thickness, 
                                           True),
                                           lines)

    
def drawLeft(x, y, width, height, depth, thickness, notch_width, lines):
    #Base line
    drawNotchedLine(genHorizontalLinePoints((width ) + OFFSET ,
                                            0,
                                            (depth),
                                            notch_width,
                                            thickness, 
                                            False),
                                            lines)
     #Right Vetical                                       
    drawNotchedLine(genVerticalLinePoints(width +  depth  + OFFSET - 2 * thickness,
                                          0,
                                          (height),
                                          notch_width, 
                                          thickness, 
                                          True), 
                                          lines)
     # Top Horizontal                                     
    drawNotchedLine(genHorizontalLinePoints(width +  (depth) + OFFSET - 2 * thickness,
                                           (height), 
                                           -(depth), 
                                           notch_width, 
                                           thickness, 
                                           False), 
                                           lines)
     # Left Vertical                                      
    drawNotchedLine(genVerticalLinePoints((width ) + OFFSET ,
                                          (height), 
                                          -(height), 
                                          notch_width, 
                                          thickness, 
                                          True), 
                                          lines)
  
def drawTop(x, y, width, depth, thickness, notch_width, lines):
    #Base Line
    drawNotchedLine(genHorizontalLinePoints(width + depth + width + (2 * OFFSET),
                                            0,
                                            -(width ),
                                            notch_width,
                                            thickness, 
                                            False),
                                            lines)
     # Right Vertical                                       
    drawNotchedLine(genVerticalLinePoints(width + depth +  width  + (2 * OFFSET),
                                          0,
                                          (depth),
                                          notch_width,
                                          thickness, 
                                          False),
                                          lines)
     #Top Horizontal                                     
    drawNotchedLine(genHorizontalLinePoints(width + depth + thickness + thickness + (2 *  OFFSET),
                                            depth - 2 * thickness,
                                            width,
                                            notch_width, 
                                            thickness,
                                            False),
                                            lines)
      #Left Vertical                                      
    drawNotchedLine(genVerticalLinePoints(width + depth + thickness + thickness + (2 * OFFSET),
                                          depth - 2 * thickness,
                                          -depth,
                                          notch_width,
                                          thickness,
                                          False),
                                          lines)

    
def drawBack(x, y, width,  height, thickness, notch_width, lines ):
    #Base Horizontal
    drawNotchedLine(genHorizontalLinePoints(x ,
                                            height + thickness,
                                            width,
                                            notch_width,
                                            thickness,
                                            True),
                                            lines)
     #Right Vertical                                       
    drawNotchedLine(genVerticalLinePoints(width,
                                          height + height + thickness,
                                          -height,
                                          notch_width,
                                          thickness,
                                          True),
                                          lines)
     # Top Horizontal                                     
    drawNotchedLine(genHorizontalLinePoints(width,
                                            height + height + thickness,
                                            -width,
                                            notch_width,
                                            thickness,
                                            True),
                                            lines)
     # Left Vertical                                       
    drawNotchedLine(genVerticalLinePoints(x,
                                          height + thickness,
                                          height,
                                          notch_width,
                                          thickness,
                                          True),
                                          lines)


def drawRight(x, y, width, height, depth, thickness, notch_width, lines):
    #Base Horizontal
    drawNotchedLine(genHorizontalLinePoints(width + OFFSET,
                                            height + OFFSET ,
                                            depth,
                                            notch_width, 
                                            thickness,
                                            False),
                                            lines)
     # Right Vertical                                       
    drawNotchedLine(genVerticalLinePoints(width + depth - 2 * thickness + OFFSET,
                                          height + OFFSET,
                                          height,
                                          notch_width,
                                          thickness,
                                          True),
                                          lines)
     #Top Horizontal                                     
    drawNotchedLine(genHorizontalLinePoints(width + depth - 2 * thickness  + OFFSET,
                                            height + height + OFFSET,
                                            -depth,
                                            notch_width, 
                                            thickness,
                                            False),
                                            lines)
     # Left Veretical                                       
    drawNotchedLine(genVerticalLinePoints(width  + OFFSET,
                                          height + height +  OFFSET,
                                          -height,
                                          notch_width,
                                          thickness,
                                          True),
                                          lines)

def drawBottom(x, y, width, depth, thickness, notch_width, lines ):
    
    #Base Horizontal
    drawNotchedLine(genHorizontalLinePoints(width + depth + width + (2 * OFFSET),
                                            depth + thickness + OFFSET,
                                            -width ,
                                            notch_width, 
                                            thickness,
                                            False),
                                            lines)
      #Right Vertical                                       
    drawNotchedLine(genVerticalLinePoints(width  + depth + width  + (2 * OFFSET),
                                          depth + thickness + OFFSET,
                                          depth ,
                                          notch_width,
                                          thickness,
                                          False),
                                          lines)
     # Top Horizontal                                     
    drawNotchedLine(genHorizontalLinePoints(width + thickness + depth + thickness + (2 * OFFSET),
                                            depth + depth - thickness + OFFSET,
                                            width ,
                                            notch_width,
                                            thickness,
                                            False),                                    
                                            lines)
     # Left Vertical                                       
    drawNotchedLine(genVerticalLinePoints(width  + depth + thickness + thickness  + (2 * OFFSET),
                                          depth  + depth - thickness + OFFSET,
                                          -depth, 
                                          notch_width,
                                          thickness,
                                          False),
                                           lines)
        





def genHorizontalLinePoints(x_origin, y_origin, length, notch_width, thickness,FullLength):
    


    notch_count = 5
        
    
    
    remaining_length = abs(length) - notch_count * notch_width
        


            

    while ( remaining_length != 0):
        
        
        if (abs(remaining_length) > (abs(2 * notch_width)) ):
            notch_count +=2
            remaining_length = remaining_length - (2 * notch_width)
            
        else:
            
            
            if(not FullLength):
                outer_notch_width = (notch_width + remaining_length / 4) - thickness
                second_notch_width = notch_width + remaining_length / 4
            else:
                
                
                outer_notch_width = notch_width + remaining_length / 4
                second_notch_width = notch_width + remaining_length / 4

            remaining_length = 0
        
        

    if (length < 0):
        
        notch_width = notch_width * -1
        outer_notch_width = outer_notch_width * -1
        second_notch_width = second_notch_width * -1
        thickness = thickness * -1
   
    notch_points = []
    
    x = x_origin 
    y = y_origin
    
    notch_points.append((x,y))
    
    
    for i in range(1, 2 * notch_count ):
        
        if (len(notch_points) % 2 == 1):
            
            if (i == 1 or i == (2 * notch_count - 1)):
                
                x =x + outer_notch_width
            elif (i == 3 or i == (2 * notch_count - 3 )):
                
                x =x + second_notch_width
            else:
                x = x + notch_width 
                
  
        if (len(notch_points) % 2 == 0):
         
            if (y == y_origin):
                y = thickness + y_origin
                
            else: 
                y = y_origin
 
        notch_points.append((x,y))
        
 
    return notch_points
     
def genVerticalLinePoints(x_origin, y_origin, length, notch_width, thickness,FullLength):  
    
    points = genHorizontalLinePoints(y_origin,x_origin, length, notch_width, thickness,FullLength)
    
    position = 0    
    for i in points:
 
        point = i
        pointX =  (point[0])
        pointY =   (point[1])
        points.pop(position)     
        points.insert(position, (pointY,pointX))       
        position +=1

    return points
            
  
    
def drawNotchedLine(points, sketch):
    
    linePoints = points    
    lines = sketch
    
    

    point1 = linePoints.pop(0)
    

    while (len(linePoints) > 0):
        
        point2 = linePoints.pop(0)
        

        lines.addByTwoPoints(adsk.core.Point3D.create(point1[0], point1[1], 0), adsk.core.Point3D.create(point2[0], point2[1], 0 ))
         
        point1 = point2


class LazerBoxMakerCommandExecuteHandler(adsk.core.CommandEventHandler):
    def notify(self, args):
        try:
            
            unitsMgr = app.activeProduct.unitsManager
            command = args.firingEvent.sender
            
            inputs = {}
            for input in command.commandInputs:
                inputs[input.id] = input
            
            # Ensure all inputs were provided
            requiredInputs = ['widthInput', 'heightInput', 'depthInput', 'materialInput','notchWidthInput']
            missingInputs = set(requiredInputs) - set(inputs.keys())
            if missingInputs:
                ui.messageBox("Missing inputs: {}".format(missingInputs))
                return
            
            # Get current design
            design = app.activeProduct
            if not design:
                 ui.messageBox('No active Fusion design', 'No design')
                 return
            
            if not inputs['componentInput'].value == '':
                    # Get the root component of the active design
                rootComp = DEFAULT_COMPONENT
                
                allOccs = rootComp.occurrences
                transform = adsk.core.Matrix3D.create()
                
                # Create a component under root component
                occ1 = allOccs.addNewComponent(transform)
                occ1.component.name = inputs['componentInput'].value
                component = occ1.component
            else:
                component = DEFAULT_COMPONENT
            # Create a new sketch on the xy plane
            sketches = DEFAULT_COMPONENT.sketches
            xzPlane = DEFAULT_COMPONENT.xZConstructionPlane
            sketch = sketches.add(xzPlane)
            lines = sketch.sketchCurves.sketchLines
            #Make it
            drawAll(0 , 0, unitsMgr.evaluateExpression(inputs['widthInput'].expression, "mm"),
                unitsMgr.evaluateExpression(inputs['heightInput'].expression, "mm"),
                unitsMgr.evaluateExpression(inputs['depthInput'].expression, "mm"),
                unitsMgr.evaluateExpression(inputs['materialInput'].expression, "mm"),
                unitsMgr.evaluateExpression(inputs['notchWidthInput'].expression, "mm"),
                lines
                )
            
            args.isValidResult = True
            
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
                    
            
class LazerBoxMakerCommandDestroyHandler(adsk.core.CommandEventHandler):
    def notify(self, args):
        try:
            # When the command is done, terminste the script
            # this will release all globals which will remove all evenrt handlers
            adsk.terminate()
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
         
            

class LazerBoxMakerCommandCreateHandler(adsk.core.CommandCreatedEventHandler):
    def notify(self, args):
        try:
            cmd = args.command
            
            onExecute = LazerBoxMakerCommandExecuteHandler()
            onDestroy = LazerBoxMakerCommandDestroyHandler()
            cmd.execute.add(onExecute)
            cmd.destroy.add(onDestroy)
            
            # keep the handler referenced globally
            handlers.append(onExecute)
            handlers.append(onDestroy)
            
            cmd.commandInputs.addValueInput(
                'widthInput',
                'Width (mm)',
                'mm',
                adsk.core.ValueInput.createByString(DEFAULT_WIDTH)
            )
            
            cmd.commandInputs.addValueInput(
                'heightInput',
                'Height (mm)',
                'mm',
                adsk.core.ValueInput.createByString(DEFAULT_HEIGHT)
            )
            cmd.commandInputs.addValueInput(
                'depthInput',
                'Depth (mm)',
                'mm',
                adsk.core.ValueInput.createByString(DEFAULT_DEPTH)
            )
            
            cmd.commandInputs.addValueInput(
                'materialInput',
                'material (mm)',
                'mm',
                adsk.core.ValueInput.createByString(DEFAULT_THICKNESS)
            )
            
            cmd.commandInputs.addValueInput(
                'notchWidthInput',
                'Notch width (mm)',
                'mm',
                adsk.core.ValueInput.createByString(DEFAULT_NOTCH_WIDTH)
            )
            
            cmd.commandInputs.addStringValueInput(
                'componentInput',
                'Component, empty for root',
                ''
            )
            
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
                

def main():
    try: 
        commandId = 'LazerBox'
        commandName = 'LazerBox'
        commandDescription = 'Create Box panels for lazer cutting'
        cmdDef = ui.commandDefinitions.itemById(commandId)
        if not cmdDef:
            cmdDef = ui.commandDefinitions.addButtonDefinition(
                commandId,
                commandName,
                commandDescription
                
            )
            
        onCommandCreated = LazerBoxMakerCommandCreateHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        
        #keep the handlers referenced globally
        handlers.append(onCommandCreated)
        
        inputs = adsk.core.NamedValues.create()
        cmdDef.execute(inputs)
        
        #prevent this module from being terminated when the script returns
        adsk.autoTerminate(False)
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
            
main()
