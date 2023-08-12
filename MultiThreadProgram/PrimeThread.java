public class PrimeThread extends Thread{
    private int taskId;
    private int sleepTime = 5000;

    public PrimeThread(int taskId) {
        this.taskId = taskId;
    }
    @Override
    public void run() {
        VerificaNumerosPrimos.test(taskId);
        try { 
            PrimeThread.sleep(sleepTime); 
        } catch (InterruptedException e) {
        }
        System.out.println(Thread.currentThread().getName() + " executando tarefa " + taskId);
    }
}
