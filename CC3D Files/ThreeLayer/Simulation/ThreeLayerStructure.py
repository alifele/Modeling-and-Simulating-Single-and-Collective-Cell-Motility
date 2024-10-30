
from cc3d import CompuCellSetup
        

from ThreeLayerStructureSteppables import ThreeLayerStructureSteppable

CompuCellSetup.register_steppable(steppable=ThreeLayerStructureSteppable(frequency=1))


CompuCellSetup.run()
