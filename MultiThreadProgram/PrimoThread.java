public class PrimoThread extends Thread{

    public void run(int i) {
        System.out.println(Thread.currentThread());
        VerificaNumerosPrimos.test(i);
    }

    @Override
    public void run() {
    }
}
