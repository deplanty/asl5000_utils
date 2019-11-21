class Vr3:
    def __init__(self):
        self.c = int()
        self.r = int()
        self.br = int()
        self.i_pmus = int()
        self.i_pmus_inc = int()
        self.i_pmus_hld = int()
        self.i_pmus_rel = int()
        self.e_pmus = int()
        self.e_pmus_inc = int()
        self.e_pmus_hld = int()
        self.e_pmus_rel = int()
        self.crf = float()

    # =========================================================================
    # = Getter and setter
    # =========================================================================

    def from_dict(self, data:dict):
        """
        Load the data from a dictionnary

        Args:
            data (dict): the data
        """

        self.c = data["c"]
        self.r = data["r"]
        self.br = data["br"]
        self.i_pmus = data["i_pmus"]
        self.i_pmus_inc = data["i_pmus_inc"]
        self.i_pmus_hld = data["i_pmus_hld"]
        self.i_pmus_rel = data["i_pmus_rel"]
        self.e_pmus = data["e_pmus"]
        self.e_pmus_inc = data["e_pmus_inc"]
        self.e_pmus_hld = data["e_pmus_hld"]
        self.e_pmus_rel = data["e_pmus_rel"]
        self.crf = data["CRF"]

    def to_dict(self):
        """
        Return the data as a dictionnary

        Returns:
            dict: the data
        """

        return {
            "c": self.c,
            "r": self.r,
            "br": self.br,
            "i_pmus": self.i_pmus,
            "i_pmus_inc": self.i_pmus_inc,
            "i_pmus_hld": self.i_pmus_hld,
            "i_pmus_rel": self.i_pmus_rel,
            "e_pmus": self.e_pmus,
            "e_pmus_inc": self.e_pmus_inc,
            "e_pmus_hld": self.e_pmus_hld,
            "e_pmus_rel": self.e_pmus_rel,
            "CRF": self.crf
        }
