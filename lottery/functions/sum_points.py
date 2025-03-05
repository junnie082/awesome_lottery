from lottery.models import Point
from members.models import Member

def sum_points(member_id):
    member = Member.objects.get(id=member_id)
    points = Point.objects.filter(member=member)
    total_points = 0
    for point in points:
        total_points += point.points

    return total_points
