package org.example;

import org.openjdk.jmh.annotations.*;

import java.util.Random;
import java.util.concurrent.TimeUnit;

@BenchmarkMode({Mode.AverageTime})
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 2, time = 1, timeUnit = TimeUnit.MILLISECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.MILLISECONDS)
@Fork(1)
public class MatrixMultiplicationBenchmarking {

    @State(Scope.Thread)
    public static class Operands {

        @Param({"10", "100","300", "500", "1000"})
        private int n;
        private double[][] a;
        private double[][] b;

        private long initialMemory;

        @Setup(Level.Trial)
        public void setup() {
            a = new double[n][n];
            b = new double[n][n];
            Random random = new Random();

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    a[i][j] = random.nextDouble();
                    b[i][j] = random.nextDouble();
                }
            }


            Runtime runtime = Runtime.getRuntime();
            runtime.gc();
            initialMemory = runtime.totalMemory() - runtime.freeMemory();
        }

        @TearDown(Level.Trial)
        public void tearDown() {
            Runtime runtime = Runtime.getRuntime();
            long finalMemory = runtime.totalMemory() - runtime.freeMemory();

            long memoryUsed = finalMemory - initialMemory;

            System.out.println("Matrix size: " + n + "x" + n);
            System.out.println("Total Memory used: " + memoryUsed / 1024 + " KB");

        }
    }

    @Benchmark
    public void multiplication(Operands operands) {
            new MatrixMultiplication().execute(operands.a, operands.b);

    }
}












