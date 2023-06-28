import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class EJ2_Coordenadas {
    public static void main(String[] args)
    {

        Random rnd = new Random();
        List<Integer> sys = new ArrayList<Integer>();
        for (int i = 0; i < 4; i++) {
            int n = rnd.nextInt(10);
            while (sys.contains(n)) {
                n = rnd.nextInt(10);
            }
            sys.add(n);
        }
        System.out.println("Número a adivinar: " + sys);

        int att = 1;
        int attps = 10; // Número de intentos
        Scanner sc = new Scanner(System.in);
        while (att <= attps) {
            System.out.print("Digite sus 4 números: ");
            String us = sc.nextLine();
            if (us.length() != 4) {
                System.out.println("Debe ingresar exactamente 4 números.");
                break;
            }

            List<Integer> us1 = new ArrayList<Integer>();
            try {
                for (int i = 0; i < 4; i++) {
                    int n = Integer.parseInt(us.substring(i, i + 1));
                    us1.add(n);
                }
            } catch (NumberFormatException e) {
                System.out.println("Debe ingresar solamente números.");
                break;
            }

            int pic = 0;
            int fij = 0;

            for (int i = 0; i < 4; i++) {
                if (us1.get(i) == sys.get(i)) {
                    fij++;
                }
                if (sys.contains(us1.get(i)) && us1.get(i) != sys.get(i)) {
                    pic++;
                }
            }

            System.out.println("Hay " + fij + " fijas y " + pic + " picas.");

            if (us1.equals(sys)) {
                System.out.println("¡Ganaste!");
                break;
            } else {
                System.out.println("Sigue intentando. Te quedan " + (attps - att) + " intentos.");
                att++;
            }

            if (att > attps) {
                System.out.println("Se acabaron tus intentos. El número era " + sys + ".");
                break;
            }
        }
        sc.close();
    }    
    
}         