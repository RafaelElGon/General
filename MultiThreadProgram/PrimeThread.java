public class PrimeThread extends Thread implements Runnable{
    private int taskId;

    public PrimeThread(int taskId) {
        this.taskId = taskId;
    }
    @Override
    public void run() {
        VerificaNumerosPrimos.test(taskId);
        System.out.println(Thread.currentThread().getName() + " executando tarefa " + taskId);
        try { Thread.sleep(5000); } catch (InterruptedException ie) { }
    }
}
