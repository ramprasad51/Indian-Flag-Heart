import javax.swing.*;
import java.awt.*;

public class JaiKarnataka extends JPanel {

    final int WIDTH = 700;
    final int HEIGHT = 700;

    final Color YELLOW = new Color(255, 215, 0);
    final Color RED = new Color(255, 0, 0);

    public JaiKarnataka() {
        setPreferredSize(new Dimension(WIDTH, HEIGHT));
        setBackground(Color.BLACK);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D) g;

        // Smooth drawing
        g2.setRenderingHint(
            RenderingHints.KEY_ANTIALIASING,
            RenderingHints.VALUE_ANTIALIAS_ON
        );

        g2.setStroke(new BasicStroke(2.5f));

        int centerX = WIDTH / 2;
        int centerY = 320;

        // Draw mathematical heart
        for (int i = 0; i < 180; i++) {

            double angle = i * (2 * Math.PI / 180);

            double x = 16 * Math.pow(Math.sin(angle), 3) * 15;

            double y = (
                13 * Math.cos(angle)
                - 5 * Math.cos(2 * angle)
                - 2 * Math.cos(3 * angle)
                - Math.cos(4 * angle)
            ) * 15;

            int previousX = centerX;
            int previousY = centerY - 40;

            // Divide each heart line into small segments
            for (int k = 1; k <= 50; k++) {

                double progress = k / 50.0;

                double currentX = x * progress;
                double currentY = 40 + (y - 40) * progress;

                int screenX = centerX + (int) currentX;
                int screenY = centerY - (int) currentY;

                // Karnataka flag colours
                if (currentY >= 0) {
                    g2.setColor(YELLOW);
                } else {
                    g2.setColor(RED);
                }

                g2.drawLine(
                    previousX, previousY,
                    screenX, screenY
                );

                previousX = screenX;
                previousY = screenY;
            }
        }

        // Kannada text
        g2.setColor(YELLOW);

        Font kannadaFont = new Font(
            "Nirmala UI",
            Font.BOLD,
            32
        );

        g2.setFont(kannadaFont);

        String message = "ಜೈ ಕರ್ನಾಟಕ!";

        FontMetrics fm = g2.getFontMetrics();

        int textX = (WIDTH - fm.stringWidth(message)) / 2;

        g2.drawString(message, textX, 650);
    }

    public static void main(String[] args) {

        JFrame frame = new JFrame("Jai Karnataka");

        JaiKarnataka artwork = new JaiKarnataka();

        frame.add(artwork);

        frame.pack();

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setLocationRelativeTo(null);

        frame.setVisible(true);
    }
}