import javax.swing.JOptionPane;

public class Traganumeros {
    public static void main (String[] args) {
        // Zona de recursos
        double Num;
        // Procesos
        Num = Double.parseDouble(JOptionPane.showInputDialog("Digite el número: "));
        // Salidas
        if (Num == (int)Num){
            if (Num % 2 == 0){
                JOptionPane.showMessageDialog(null, "Me comi un par.");
            } else {
                JOptionPane.showMessageDialog(null, "Me comi un impar.");
            }
        } else {
            JOptionPane.showMessageDialog(null, "Solo como enteros.");
        }
    }
}