import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Variado {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        ArrayList<String> names = new ArrayList<String>();
        ArrayList<String> ids = new ArrayList<String>();
        ArrayList<String> psswds = new ArrayList<String>();
    
        System.out.print("¿Cuántas personas desea guardar? ");
        int n = sc.nextInt();
    
        for (int i = 0; i < n; i++) {
            // Entrada de usuarios
            System.out.print("Usuario " + (i + 1) + ". Digite su nombre completo: ");
            String name = sc.next();
            System.out.print("Usuario " + (i + 1) + ". Digite su id: ");
            String id = sc.next();
    
            // Creación de clave
            String[] split = name.split(" ");
            String psswd = "";
            for (int j = 0; j < split.length; j++) {
                psswd += split[j].charAt(0);
            }
            for (int j = 0; j < 3; j++) {
                psswd += rand.nextInt(10);
            }
    
            // Verificación de clave y ID
            if (!psswds.contains(psswd) && !ids.contains(id)) {
                names.add(name);
                ids.add(id);
                psswds.add(psswd);
            } else {
                System.out.println("Se esta repitiendo una contraseña o un ID.");
                i--;
            }
        }
    
        // Salidas
        for (int i = 0; i < n; i++) {
            System.out.println("Id: " + ids.get(i) + ", Nombre: " + names.get(i) + ", Contraseña: " + psswds.get(i));
        }
    
        sc.close();
    }
    
}
