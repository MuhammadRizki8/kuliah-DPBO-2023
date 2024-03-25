package synchronization.ViewModel;

import synchronization.ViewModel.Handler;
import synchronization.Model.Player;
import synchronization.View.Display;
import synchronization.Model.GameObject;

import java.awt.Canvas;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.image.BufferStrategy;
import synchronization.Model.ID;

import synchronization.ViewModel.Controller;
import synchronization.View.Display;

public class Game extends Canvas implements Runnable
{
    public static final int width = 640;
    public static final int height = 480;
    private Display display;

    private boolean running;
    private Handler handler;
    private Thread thread;

    private boolean startCounting = false;
    private int score = 0;
    private int counter = 0;
    private int stateCounter = 0;
    private int direction = 0;
    
    public Game()
    {
        try
        {
            display = new Display(width, height, "Synchronization Tutorial");
            display.open(this); 

            handler = new Handler();

            this.setFocusable(true);
            this.requestFocus();
            this.addKeyListener(new Controller(this, handler));

            running = true;
            if (running)
            {
                handler.addObject(new Player(500, 100, ID.Player));
            // Add Floor Object
//            handler.addObject(new Floor(0, Game.HEIGHT-70, ID.Floor));
            }
        }
        catch (Exception e)
        {
            System.err.println("Failed to instantiate data.");
        }
    }
    
    public boolean isRunning()
    {
        return running;
    }

    public void setRunning(boolean running)
    {
        this.running = running;
    }
    
    public int getScore()
    {
        return score;
    }

    public void setScore(int score)
    {
        this.score = score;
    }

    public static int clamp(int var, int min, int max)
    {
        if (var >= max)
        {
            return var = max;
        }
        else if (var <= min)
        {
            return var = min;
        }
        
        return var;
    }

    public void close()
    {
        display.close();
    }

    public synchronized void start()
    {
        thread = new Thread(this);
        thread.start();
        running = true;
    }

    public synchronized void stop()
    {
        try
        {
            thread.join();
            running = false;
        }
        catch (InterruptedException e)
        {
            System.out.println("Thread error: " + e.getMessage());
        }
    }

    public void render()
    {
        BufferStrategy bs = this.getBufferStrategy();
        if (bs == null)
        {
            this.createBufferStrategy(3);
            return;
        }

        Graphics g = bs.getDrawGraphics();
        Image bg = Toolkit.getDefaultToolkit().getImage(getClass().getResource("/assets/game.jpg"));
        g.drawImage(bg, 0, 0, null);
        
        if (running)
        {
            handler.render(g);
            Font oldFont = g.getFont();
            Font newFont = oldFont.deriveFont(oldFont.getSize() * 1.3f);
            g.setFont(newFont);
            
            g.setColor(Color.blue);
            g.drawString("Score: " + score, 20, 30);
        }
        g.dispose();
        bs.show();
    }
    
    public void loop() {
        GameObject player = null;
        GameObject target = null;
        GameObject obstacle = null;

        handler.loop();

        if (running) {
            counter++;
            if (startCounting) {
                stateCounter++;
            }

            if (stateCounter >= 40) {
                stateCounter = 0;
                startCounting = false;
            }

            if (counter >= 50) {
                direction = (direction == 0) ? 1 : 0;
                counter = 0;
            }

            for (int i = 0; i < handler.count(); i++) {
                GameObject gameObject = handler.get(i);
                if (gameObject.getType().equals("Player")) {
                    player = gameObject;
                } else if (gameObject.getType().equals("Target")) {
                    target = gameObject;
                } else if (gameObject.getType().equals("Obstacle")) {
                    obstacle = gameObject;
                }
            }

            handler.makan(player, target);

        }
    }

    
    @Override
    public void run()
    {
        double fps = 60.0;
        double ns = (1000000000 / fps);
        double delta = 0;

        long time = System.nanoTime();
        long now = 0;
        long timer = System.currentTimeMillis();

        int frames = 0;
        int obstacleCounter = 0; // Counter for adding obstacles
        int obstacleDelay = 60; // Delay between adding obstacles (in frames)

        while (running)
        {
            now = System.nanoTime();
            delta += ((now - time) / ns);
            time = now;

            while (delta > 1)
            {
                loop();
                delta--;
            }

            if (running)
            {
                render();
                frames++;
            }

            if ((System.currentTimeMillis() - timer) > 1000)
            {
                timer += 1000;
                frames = 0;
            }

            obstacleCounter++;
            if (obstacleCounter >= obstacleDelay)
            {
                int x = 0;
                int y = height;
                int obstacleWidth = (int) (Math.random() * 590); // Random width from 100 to 500
                handler.addObstacle(x, y, obstacleWidth);
                obstacleCounter = 0; // Reset the counter
                obstacleDelay = 300; // Randomize the delay between obstacles (1 to 2 seconds)
            }
        }

        stop();
    }

    void increment() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
