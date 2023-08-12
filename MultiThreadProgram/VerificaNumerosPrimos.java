public class VerificaNumerosPrimos {
    public static boolean isPrimo(int num) {
        if (num <= 1) {
            return false;
        } else if (num <= 3) {
            return true;
        }
        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static void test(int i) {
        if (isPrimo(i)) {
            System.out.println(i + " é primo");
        } else {
            System.out.println(i + " não é primo");
        }
    }
}

