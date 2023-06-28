import javax.swing.JOptionPane;

public class Sort {
    public static void main (String[] args) {
        // Zona de recursos
        float Num1, Num2, Num3, Sort1, Sort2;
        // Procesos
        Num1 = Float.parseFloat(JOptionPane.showInputDialog("Digite el primer número: "));
        Num2 = Float.parseFloat(JOptionPane.showInputDialog("Digite el segundo número: "));
        Num3 = Float.parseFloat(JOptionPane.showInputDialog("Digite el tercer número: "));
        // Salidas
        Sort1 = Math.max(Num1, Num2);
        Sort2 = Math.max(Sort1, Num3);
        JOptionPane.showMessageDialog(null, "El número más grande es:" + Sort2);
    }
}