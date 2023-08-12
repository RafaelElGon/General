public class PrimoThread extends Thread implements Runnable{
    private int taskId;

    public PrimoThread(int taskId) {
        this.taskId = taskId;
    }
    @Override
    public void run() {
        VerificaNumerosPrimos.test(taskId);
        System.out.println(Thread.currentThread().getName() + " executando tarefa " + taskId);
        try { Thread.sleep(5000); } catch (InterruptedException ie) { }
    }
}
