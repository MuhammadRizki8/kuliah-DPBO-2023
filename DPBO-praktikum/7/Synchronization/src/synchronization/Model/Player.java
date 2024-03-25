/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package synchronization.Model;

import java.awt.Graphics;
import java.awt.Color;
import synchronization.ViewModel.Game;

/**
 *
 * @author Ghifari Octaverin
 */
public class Player extends GameObject {
    // Constructor
    public Player(int x, int y, ID id) {
        super(x, y, id);
        jumping = false;
        vel_x = 0;
    }
    
    // Update Player per Tick
    @Override
    public void tick() {
        // When Player is Jumping
        if (jumping && vel_y < 30) {
            vel_y = -15;
            vel_x = -5;
        }

        // When Player is Moving to Right
        if (right) {
            vel_x += 5;
        }

        // When Playing is Moving to Left
        if (left) {
            vel_x -= 5;
        }

        x += vel_x;
        y += vel_y;
        
        // Gravity System
        gravity = 5;
        if (falling && vel_y < gravity) {
            vel_y += 3;
        } else if (!falling && vel_y > 0) {
            vel_y = 0;
        }

        // When Player Reach Screen Size Limit
        if (x < 0) {
            x = 0;
        }

        if (y > Game.HEIGHT - 80) {
            y = Game.HEIGHT - 80;
        }

        if (y < 0) {
            y = 0;
        }

        vel_x = 0;
    }
    
    // Render Player
    @Override
    public void render(Graphics g) {
        g.setColor(Color.decode("#FBCB0A"));
        g.fillOval(x, y, 30, 30);
    }
}