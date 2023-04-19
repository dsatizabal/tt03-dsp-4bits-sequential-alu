`timescale 1ns / 1ps

module dsp_4its_seq_alu(input [7:0] io_in, output [7:0] io_out);

   wire clk			   = io_in[0];
   wire reset			= io_in[1];
   wire [3:0]data_in	= io_in[7:4];

   reg [3:0] result;
   reg [3:0] sign_zero_carry_done;
   assign io_out = { sign_zero_carry_done, result };

   reg [3:0] alu_state;
   reg [3:0] op1;
   reg [3:0] op2;
   reg [3:0] operation;

   localparam GET_FIRST_OPERAND         = 4'b0000;
   localparam GET_SECOND_OPERAND        = 4'b0001;
   localparam GET_AND_PERFORM_OPERATION = 4'b0010;

   always @(posedge clk) begin
      if (reset) begin
         alu_state <= GET_FIRST_OPERAND;
         sign_zero_carry_done <= 4'b0000;
         result <= 4'b0000;
      end else begin
         case (alu_state)
            GET_FIRST_OPERAND: begin
               op1 <= data_in;
               alu_state <= GET_SECOND_OPERAND;
            end
            GET_SECOND_OPERAND: begin
               op2 <= data_in;
               alu_state <= GET_AND_PERFORM_OPERATION;
            end
            GET_AND_PERFORM_OPERATION: begin
               operation <= data_in;
               case(operation)
                  4'b0000: begin
                     if (op1 + op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     result = A + B;
                  end
                  4'b0001: begin
                     if (op1 < op2) sign_zero_carry_done[3] = 1'b1;
                     if (op1 == op2) sign_zero_carry_done[2] = 1'b1;
                     result = A - B;
                  end
                  4'b0010: begin
                     if (op1 & op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (op1 & op2 == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = A & B;
                  end
                  4'b0011: begin
                     if (op1 | op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (op1 | op2 == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = A | B;
                  end
                  4'b0100: begin
                     if (~op1 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (~op1 == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = ~A;
                  end
                  4'b0101: begin
                     if (~(op1 & op2) > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (~(op1 & op2) == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = A & B;
                  end
                  4'b0110: begin
                     if (~(op1 | op2) > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (~(op1 | op2) == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = A | B;
                  end
                  default: begin
                    if (op1 + op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                    result = A + B ;
                  end
               endcase

                sign_zero_carry_done[0] = 1'b1;
                alu_state <= GET_FIRST_OPERAND;
            end
         endcase
      end
    end

endmodule
