`default_nettype none
`timescale 1ns/1ns

/*
this testbench just instantiates the module and makes some convenient wires
that can be driven / tested by the cocotb test.py
*/

module tb (
    // testbench is controlled by test.py
    input clk,
    input reset,
    input enabled,
    input [3:0] data,
    output [7:4] result,
    output [3:0] flags
   );

    // this part dumps the trace to a vcd file that can be viewed with GTKWave
    initial begin
        $dumpfile ("tb.vcd");
        $dumpvars (0, tb);
        #1;
    end

    // wire up the inputs and outputs
    wire [7:0] inputs = {data, 1'b0, enabled, reset, clk};
    wire [7:0] outputs;
    assign flags = outputs[7:4];
    assign result = outputs[3:0];

    // instantiate the DUT
    dsp_4bits_seq_alu dsp_4bits_seq_alu(
        `ifdef GL_TEST
            .vccd1( 1'b1),
            .vssd1( 1'b0),
        `endif
        .io_in  (inputs),
        .io_out (outputs)
        );

endmodule
