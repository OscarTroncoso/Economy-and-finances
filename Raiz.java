import javax.swing.JOptionPane;

public class Raiz {
    public static void main (String[] args) {
        // Zona de recursos
        double Ind, Rad, Rai;
        // Procesos
        Ind = Float.parseFloat(JOptionPane.showInputDialog("Digite el indice: "));
        Rad = Float.parseFloat(JOptionPane.showInputDialog("Digite el radicando: "));
        // Salidas
        if (Ind == 0){
            JOptionPane.showMessageDialog(null, "El indice no puede ser 0 (inderteminado).");
        }
        else{
            Rai = Math.pow(Rad, Ind);
            if (Ind > 0 & Rad > 0){
                JOptionPane.showMessageDialog(null, "La raiz es: " + Rai);
            }
            if (Ind < 0 & Rad > 0){
                JOptionPane.showMessageDialog(null, "La raiz es: " + Rai);
            }
            if (Ind < 0 & Rad < 0){
                JOptionPane.showMessageDialog(null, "La raiz es: " + Rai + " de un número complejo.");
            }
            if (Ind > 0 & Rad < 0){
                JOptionPane.showMessageDialog(null, "La raiz es: " + Rai + " de un número complejo.");
            }
            if (Rad == 0 & Ind != 0){
                JOptionPane.showMessageDialog(null, "La raiz es: " + Rai);
            }
        }
    }
}