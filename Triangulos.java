import javax.swing.JOptionPane;

public class Triangulos {
    public static void main (String[] args) {
        // Zona de recursos
        float A1, A2, A3;
        // Procesos
        A1 = Float.parseFloat(JOptionPane.showInputDialog("Digite el primer ángulo: "));
        A2 = Float.parseFloat(JOptionPane.showInputDialog("Digite el segundo ángulo: "));
        A3 = Float.parseFloat(JOptionPane.showInputDialog("Digite el tercer ángulo: "));
        // Salidas
        if ((A1 + A2 + A3) == 180){
            if (A1 == 90 || A2 == 90 || A3 == 90){
                JOptionPane.showMessageDialog(null,"Es un triángulo rectángulo.");
            } if (A1 > 90 || A2 > 90 || A3 > 90) {
                JOptionPane.showMessageDialog(null,"Es un triángulo obtusángulo.");
            } if (A1 < 90 & A2 < 90 & A3 < 90) {
                JOptionPane.showMessageDialog(null,"Es un triángulo acutángulo.");
            }
        } else {
            JOptionPane.showMessageDialog(null, "La suma de sus ángulos no corresponde a un triángulo.");
        }
    }
}