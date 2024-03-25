package synchronization.ViewModel;

import java.awt.Graphics;
import java.util.LinkedList;
import synchronization.Model.GameObject;

/**
 *
 * @author Ghifari Octaverin
 */
public class Handler {
    LinkedList<GameObject> obj = new LinkedList<>();
    
    // Update Game Object Per Tick
    public void tick() {
        for (int i = 0; i < obj.size(); i++) {
            GameObject tmpObj = obj.get(i);
            tmpObj.tick();
        }
    }
    
    // Render Game Object
    public void render(Graphics g) {
        for (int i = 0; i < obj.size(); i++) {
            GameObject tmpObj = obj.get(i);
            tmpObj.render(g);
        }
    }
    
    // Add Object To List
    public void addObject(GameObject obj) {
        this.obj.add(obj);
    }
    
    // Remove Object From List
    public void removeObject(GameObject obj) {
        this.obj.remove(obj);
    }
    
    // Count List Size
    public int countObject() {
        return this.obj.size();
    }
}