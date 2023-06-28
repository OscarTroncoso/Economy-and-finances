import javax.swing.JOptionPane;

public class EJ2_Cuadratica {
    public static void main (String[] args) {
        // Zona de recursos
        float a,b,c,X1,X2,d,pr, pi;
        // Procesos
        a = Float.parseFloat(JOptionPane.showInputDialog("Digite el coeficiente a : "));
        b = Float.parseFloat(JOptionPane.showInputDialog("Digite el coeficiente b: "));
        c = Float.parseFloat(JOptionPane.showInputDialog("Digite el coeficiente c: "));

        // Cálculos y salidas
        if(a!=0){
            d = (float)(Math.pow(b, 2)-4 * a * c);
            if(d>0){
                X1 = (float)((-b+Math.sqrt(d))/(2*a));
                X2 = (float)((-b-Math.sqrt(d))/(2*a));
                System.out.println("X1 =" +X1+ "X2 ="  +X2);

            }
            else{
                if(d==0){
                    X1 =-b/2*a;
                    System.out.println("X1 =" +X1); 
                }
                else{
                    d = -d;
                    pr = -b/2*a;
                    pi = (float)(Math.sqrt(d)/2*a);
                    System.out.println("X1 ="  +pr+ "+"+pi+"i" + "X2 =" +pr+"-"+pi+"i");
                }
            }
        }
        else{
            X1 = -c/b;
            System.out.println("X1=" +X1);
        }
    }
}