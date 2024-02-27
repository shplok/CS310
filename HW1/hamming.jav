public class HammingWeight {

    public static int hammingSequential(int n) {
        int count = 0;
        while (n != 0) {
            count += n & 1;
            // shift n to the right 1
            n >>= 1;
        }
        return count;
    }

    public static int hammingDivide(int n) {
        if (n == 0) {
            return 0;
        } else {
            return (n & 1) + hammingDivide(n >> 1);
        }
    }

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java HammingWeight <integer> <method>");
            return;
        }

        int n = Integer.parseInt(args[0]);
        String seqOrDiv = args[1].toLowerCase();

        int result = 0;
        if (seqOrDiv.equals("sequential")) {
            result = hammingSequential(n);
        } else if (seqOrDiv.equals("divide_and_conquer")) {
            result = hammingDivide(n);
        } else {
            System.out.println("Error: Invalid method specified.");
            return;
        }
        System.out.println("Number of '1' bits (Hamming weight): " + result);
    }
}
