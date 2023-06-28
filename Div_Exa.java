import javax.swing.JOptionPane;

public class Div_Exa {
    public static void main (String[] args) {
        // Zona de recursos
        double Num, Den;
        // Procesos
        Num = Float.parseFloat(JOptionPane.showInputDialog("Digite el numerador: "));
        Den = Float.parseFloat(JOptionPane.showInputDialog("Digite el denominador: "));
        // Cálculos y salidas
        if ((Num % Den) == 0){
            JOptionPane.showMessageDialog(null, Num + " es perfectamente divisble entre " + Den);
        } else {
            JOptionPane.showMessageDialog(null, Num + " no es perfectamente divisble entre " + Den);
        }
    }
}
