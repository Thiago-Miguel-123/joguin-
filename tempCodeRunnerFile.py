    def recalcStacks(self,stacks):
        if stacks >= self.maxStack:
                stacks = stacks - self.maxStack
                self.stacks-= stacks
                