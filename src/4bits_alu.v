`timescale 1ns/1ns

module dsp_4bits_seq_alu(input [7:0] io_in, output [7:0] io_out);

   wire clk			   = io_in[0];
   wire reset			= io_in[1];
   wire process		= io_in[2];
   wire [3:0]data_in	= io_in[7:4];

   reg [3:0] result;
   reg [3:0] sign_zero_carry_done;
   assign io_out = { sign_zero_carry_done, result };

   reg [3:0] alu_state;
   reg [3:0] op1;
   reg [3:0] op2;
   reg [3:0] operation;

   localparam GET_FIRST_OPERAND         = 4'b0001;
   localparam GET_SECOND_OPERAND        = 4'b0010;
   localparam GET_OPERATION             = 4'b0100;
   localparam PERFORM_OPERATION         = 4'b1000;

   always @(posedge clk) begin
      if (reset) begin
         sign_zero_carry_done <= 4'b0000;
         alu_state <= GET_FIRST_OPERAND;
         result <= 4'b0000;
      end else begin
         if (process) begin
            case (alu_state)
               GET_FIRST_OPERAND: begin
                  op1 <= data_in;
                  alu_state <= GET_SECOND_OPERAND;
                  sign_zero_carry_done <= 4'b0000;
               end
               GET_SECOND_OPERAND: begin
                  op2 <= data_in;
                  alu_state <= GET_OPERATION;
               end
               GET_OPERATION: begin
                  operation <= data_in;
                  alu_state <= PERFORM_OPERATION;
               end
               PERFORM_OPERATION: begin
                  case(operation)
                     4'b0000: begin
                        if (op1 + op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                        result <= op1 + op2;
                     end
                     4'b0001: begin
                        if (op1 < op2) sign_zero_carry_done[3] = 1'b1;
                        if (op1 == op2) sign_zero_carry_done[2] = 1'b1;
                        result <= op1 - op2;
                     end
                     4'b0010: begin
                        if (op1 & op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                        if (op1 & op2 == 4'h0) sign_zero_carry_done[2] = 1'b1;
                        result <= op1 & op2;
                     end
                     4'b0011: begin
                        if (op1 | op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                        if (op1 | op2 == 4'h0) sign_zero_carry_done[2] = 1'b1;
                        result <= op1 | op2;
                     end
                     4'b0100: begin
                        if (~op1 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                        if (~op1 == 4'h0) sign_zero_carry_done[2] = 1'b1;
                        result <= ~op1;
                     end
                     4'b0101: begin
                        if (~(op1 & op2) > 4'hF) sign_zero_carry_done[1] = 1'b1;
                        if (~(op1 & op2) == 4'h0) sign_zero_carry_done[2] = 1'b1;
                        result <= op1 & op2;
                     end
                     4'b0110: begin
                        if (~(op1 | op2) > 4'hF) sign_zero_carry_done[1] = 1'b1;
                        if (~(op1 | op2) == 4'h0) sign_zero_carry_done[2] = 1'b1;
                        result <= op1 | op2;
                     end
                  endcase

                  sign_zero_carry_done[0] <= 1'b1;
                  alu_state <= GET_FIRST_OPERAND;
               end
            endcase
         end
      end
    end

endmodule
