from .models import Per_Notice_Pair, First_Notice_Pair, Agreement, Agreement_Status
from notice.models import First_Notice, Periodical_Notice, Notice_Status

# def assign_agreement_id(pairs, agr_id):
#     agreement = Agreement.objects.get(id=agr_id)
#     for pair in pars:
#         pair.agreement = agreement

def do_create_agreement_per(notices, agreement):
    # pair foreign key assignment
    for notice in notices:
        print("1")
        pairs = Per_Notice_Pair.objects.filter(new_notice__id=notice.id)
        for pair in pairs:
            print("2")
            pair.agreement = agreement
            pair.save()


    