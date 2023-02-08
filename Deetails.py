import PySimpleGUIQt as S

class Deetails:
    def __init__(self):
        form = S.FlexForm('Transaction Details')
        layout = [[S.Text("Sender's Name:"), S.InputText()],
        [S.Text("Recipient's Name:"), S.InputText()],
        [S.Text("Amount:"), S.InputText()],
        [S.OK()]]
        
        self.button, self.values = form.Layout(layout).Read()

        self.name, self.name2, self.amount = self.values.values()

    
    def transactionDetails(self):
        return f"{self.name} sent {self.name2} {self.amount}."


#var = Detai()

#print(var.transactionDetails())






